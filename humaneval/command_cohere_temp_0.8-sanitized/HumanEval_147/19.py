def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate max triples where a[i] + a[j] + a[k] is a multiple of 3
    # by considering all possible triples with i < j < k
    def max_triples_num(array, num):
        if num == 1:
            return array.count(0) // 3
        elif num == 2:
            return sum(array.count(x) for x in array if x % 2 == 0) // 2
        else:
            return sum(array.count(x) for x in array if x % 4 == 0) // 4
    
    return max_triples_num(arr, n - 2)