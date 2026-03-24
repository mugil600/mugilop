class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data),
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data),
        preorder(root.left)
        preorder(root.right)
def postorder(root):
     if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(3)
print ("Binary Tree")
root.PrintTree()
print ("\nInorder")
inorder(root)
print ("Preorder")
preorder(root)
print ("\nPostorder")
postorder(root)
