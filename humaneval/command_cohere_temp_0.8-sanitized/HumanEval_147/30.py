def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum number of triples where a[i] + a[j] + a[k] is a multiple of 3.
    # We count the number of multiples of 3, then double it. There are three ways to pick three elements.
    count_three = sum(1 for x in arr if x % 3 == 0)
    return count_three // 3 * 2