
class Tree:
    def __init__(self, root):
        self.root = root  # root is a dictionary node

    def get_element_by_id(self, element_id):
        """
        Depth-first search for a node with a matching 'id'.
        Returns the node dictionary if found, else None.
        """
        def dfs(node):
            if node['id'] == element_id:
                return node
            for child in node.get('children', []):
                found = dfs(child)
                if found:
                    return found
            return None

        return dfs(self.root)