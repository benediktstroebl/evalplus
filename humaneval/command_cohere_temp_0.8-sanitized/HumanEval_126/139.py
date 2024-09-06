import heapq
def is_sorted(lst):
    return len(set(lst)) == len(lst) and all(True for _ in heapq.nsmallest(len(lst), lst))