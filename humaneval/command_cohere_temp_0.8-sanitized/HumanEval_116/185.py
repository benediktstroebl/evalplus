def count_ones(n):
    return bin(n).count("1")
def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr