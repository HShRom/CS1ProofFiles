class BST():
    def __init__(self):
        self.root = None
        self.size = 0


class TN():
    def __init__(self, key , val = 0):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


#Exam test - should be 8
# tn5, tn4, tn3, tn2, tn1, tn6 = TN(5), TN(4), TN(3), TN(2), TN(1), TN(6)
# tn1.left = tn2
# tn1.right = tn5
# tn2.right = tn4
# tn2.left = tn3
# tn5.right = tn6
# T_exam = BST()
# T_exam.root = tn1

## My own test - should be 28.
tn5, tn4, tn3, tn2, tn1, tn6 = TN(5), TN(4), TN(3), TN(2), TN(1), TN(6)
tn7, tn8, tn9, tn10, tn11, tn12 = TN(5), TN(4), TN(3), TN(2), TN(1), TN(6)
tn1.left, tn1.right = tn2, tn3
tn2.left = tn4
tn4.left, tn4.right = tn7, tn8
tn7.left, tn7.right = tn11, tn12
tn3.left, tn3.right = tn5, tn6
tn5.left = tn9
tn6.right = tn10
T_home = BST()
T_home.root = tn1

def sd(T):
    return sdn(T.root, 0)

def sdn(node, depth):
    left_exists = node.left!=None
    right_exists = node.right!=None
    sum = 0
    if left_exists:
        sum += depth + 1 + sdn(node.left, depth+1)
    if right_exists:
        sum+= depth + 1 + sdn(node.right, depth+1)
    return sum


print(sd(T_home))