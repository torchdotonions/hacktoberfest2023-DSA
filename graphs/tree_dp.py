class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children else []

def diameter_of_tree(root):
    def dfs(node):
        nonlocal diameter
        nonlocal max_depth

        max_depths = [0, 0]  # The two highest depths

        for child in node.children:
            depth = dfs(child) + 1

            if depth > max_depths[0]:
                max_depths[0], max_depths[1] = depth, max_depths[0]
            elif depth > max_depths[1]:
                max_depths[1] = depth

            diameter = max(diameter, max_depths[0] + max_depths[1])

        return max_depths[0]

    diameter = 0
    max_depth = dfs(root)
    return diameter

# Example usage
root = TreeNode(1, [
    TreeNode(2, [
        TreeNode(4),
        TreeNode(5),
    ]),
    TreeNode(3),
])

result = diameter_of_tree(root)
print("The diameter of the tree is:", result)
