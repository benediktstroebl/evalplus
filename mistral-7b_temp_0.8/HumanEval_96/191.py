
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    #hint: use the sieve of eratosthenes to check if a number is prime or not
    #hint: use a while loop to iterate from 2 to n
    #hint: make a new array to store the prime numbers
    #hint: initialize the array with 0 and the length of the array is n+1
    #hint: use the while loop to check if the number is prime or not
    #hint: if the number is prime, add it to the new array and increment the counter
    #hint: return the new array
    count = 0
    list1 = []
    list2 = [False]*(n+1)
    for i in range(2,n):
        if not list2[i]:
            count += 1
            list1.append(i)
            for j in range(i*i,n+1,i):
                list2[j] = True
    return list1

