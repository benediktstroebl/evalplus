import heapq
def pluck(arr):
    even_nodes = [i for i in arr if i % 2 == 0]
    if even_nodes: 
        min_heap = []
        heapq.heappush(min_heap, [arr[0], 0])
        for i in range(1, len(arr)):
            node_value, index = heapq.heappop(min_heap)
            if arr[i] == node_value: 
                heapq.heappush(min_heap, [arr[i], i])
        return heapq.heappop(min_heap)[1:]
    else: 
        return []