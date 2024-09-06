import heapq
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if even_nodes: 
        min_heap = []
        for node in even_nodes:
            heapq.heappush(min_heap, node)
        heapq.heappop(min_heap)
        return [heapq.heappop(min_heap), min_heap[0][0]]
    else:
        return []