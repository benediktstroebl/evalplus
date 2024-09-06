from collections import Counter
def pluck(arr):
    # Count the nodes with smallest even values and their positions
    evects = Counter(x for x in arr if x % 2 == 0)
    # Get the node with the smallest index from the Counter result
    node_to_pluck = min(evects.items(), key=lambda x: x[1])[0]
    # Return the node in the required format
    return [node_to_pluck, node_to_pluck['count']]