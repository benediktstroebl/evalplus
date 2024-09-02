
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    # A dictionary of already visited nodes
    visited = {}
    # A stack to keep track of the current node
    stack = []
    # A queue to hold the next node to visit
    queue = []
    # Current node
    current = ''
    # Length of the current node
    current_len = 0
    # This is used to check if the current node is happy
    is_happy = False
    
    while stack or queue:
        # If the stack or queue are empty, pop the next element from the other one
        if not stack:
            node = queue.pop(0)
            node_len = len(node)
            # Check if the current node is the same as the node
            if node == current:
                # If they are the same, increment the current node's length
                current_len += 1
                # If the current node is longer than the node, increment the length of the node
                if current_len > node_len:
                    node += current[current_len - node_len:]
                    current_len -= node_len
                    # If the current node is happy, return True
                    if current_len == 0:
                        return True
                    # If the current node is not happy, remove it from the stack and add it to the queue
                    stack.remove(current)
                    queue.append(current)
            # Check if the current node is in the dictionary of visited nodes
            if current in visited:
                # If it is, pop the node from the visited dictionary
                node = visited[current]
                stack.remove(node)
                # Add the current node to the stack
                stack.append(current)
            else:
                # If it is not, add the current node to the dictionary of visited nodes
                visited[current] = node = current
                stack.append(node)
        # If the queue is empty, add the next element to the queue
        if not queue:
            node = stack.pop(0)
            node_len = len(node)
            # Check if the current node is the same as the node
            if node == current:
                # If they are the same, increment the current node's length
                current
