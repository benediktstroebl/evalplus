def largest_prime_factor(n: int):
    if n <= 1:
        return 1
    if n <= 3:
        return 3
    #iteratively find the largest prime factor
    for i in range(5,int(n**.5)+1,6):
        if n%i == 0:
            return i
    return 4 #if no solution is found