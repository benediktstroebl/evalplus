def strange_sort_list(lst):
    # Using heapq to generate the desired sorting
    return [x for x in heapq.heapify(lst) if x != heapq.nsmallest(2, lst)]