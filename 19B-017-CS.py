class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def Balance(self, root):
        if root == None:
            return 0
        return self.Height(root.left) - self.Height(root.right)

    def Height(self,root):
        if root == None:
            return 0
        return root.height


    def rotateRight(self, root):
        x = root.left
        y = x.right
        x.right = root
        root.left = y
        root.height = max(self.Height(root.left), self.Height(root.right)) + 1
        x.height = max(self.Height(x.left), self.Height(x.right)) + 1
        return x

    def rotateLeft(self, root):
        x = root.right
        y = x.left
        x.left = root
        root.right = y
        root.height = max(self.Height(root.left), self.Height(root.right)) + 1
        x.height = max(self.Height(x.left), self.Height(x.right)) + 1
        return x


    def __FindMin(self, root):
        if root.left == None:
            return root
        return self.__FindMin(root.left)


    def PreOrder(self):
        print(self.root.height)
        print("Root Value", self.root.value)
        return self.__PreOrder(self.root) ,

    def __PreOrder(self, root):
        if root:
            print(root.value, end=" ")
            self.__PreOrder(root.left)
            self.__PreOrder(root.right)


    def Insert(self, value):
        self.root = self.__Insert(self.root, value)

    def __Insert(self, root, value):
        if root == None:
            root = Node(value)

        elif value > root.value:
            root.right = self.__Insert(root.right, value)
        else:
            root.left = self.__Insert(root.left, value)

        root.height = 1 + max(self.Height(root.left), self.Height(root.right))

        balance = self.Balance(root)

        # left left
        if balance > 1 and value < root.left.value:
            return self.rotateRight(root)

            # right right
        if balance < -1 and value > root.right.value:
            return self.rotateLeft(root)

            # left right
        if balance > 1 and value > root.left.value:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

            # right left
        if balance < -1 and value < root.right.value:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root


    def Delete(self, value):
        return self.__Delete(self.root, value)

    def __Delete(self, root, value):
        if root == None:
            return root

        if value > root.value:
            root.right = self.__Delete(root.right, value)

        elif value < root.value:
            root.left = self.__Delete(root.left, value)

        else:
            if root.left == None: return root.right

            if root.right == None: return root.left


            y = self.__FindMin(root.right)
            root.value = y.value
            root.right = self.__Delete(root.right, y.value)


        root.height = 1 + max(self.Height(root.left), self.Height(root.right))

        balance = self.Balance(root)

            # right left
        if balance < -1 and self.Balance(root.left) > 0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
            # right right
        if balance < -1 and self.Balance(root.right) <= 0:
            return self.rotateLeft(root)
            # left left
        if balance > 1 and self.Balance(root.left) >= 0:
            return self.rotateRight(root)
            # left right
        if balance > 1 and self.Balance(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        return root



obj = AVL()
obj.Insert(10)
obj.Insert(23)
obj.Insert(22)
obj.Insert(25)
obj.Insert(0)
obj.Insert(11)
obj.Insert(-1)
obj.Insert(1)
obj.Insert(2)
obj.PreOrder()
print()
obj.Delete(11)
print("\nAfter Deleting")
obj.PreOrder()