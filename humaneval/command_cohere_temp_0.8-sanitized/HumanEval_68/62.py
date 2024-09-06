import heapq
def pluck(arr):
    even_nodes = [i for i in arr if i % 2 == 0]
    if even_nodes:
        # Use heapq to find the smallest even node and its index
        heap = [(n, i) for i, n in enumerate(even_nodes)]
        heapq.heapify(heap)
        smallest_node, smallest_index = heapq.heappop(heap)
        
        return [smallest_node, smallest_index]
    else:
        return []