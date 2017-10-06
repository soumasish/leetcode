"""Created by sgoswami on 9/14/17."""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def findSecondLargestElement(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root.right.left and not root.right.right:
            return root
        self.findSecondLargestElement(root.right)
