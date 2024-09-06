```python
def count_palindromes(n):
    # collect all the integers from 1 to n inclusive, and their parities
    integers = list(range(1, n+1))
    even, odd = 0, 0
    for num in integers:
        if num == int(str(num)[:-1] + str(num) [-1]:):
            parity = 1 if num % 2 == 0 else 2
            num_list, parity_list = [], []
            for i in range(parity):
                num_list.append(integers[:int(len(integers) / 2)]);
                parity_list.append(parity)
            if num_list == parity_list:
                if parity == 1:
                    even += 1
                else:
                    odd += 1
        integers = integers[:len(integers) - 1]
    return even, odd

n = int(input())
even, odd = count_palindromes(n)
print(f'({even}, {odd})')
```
The above count_palindromes() function takes an integer n and returns a tuple with the count of even and odd integer palindromes, respectively. The code first collects all the integers from 1 to n inclusive and their parities using the list(range(1, n+1)) and two variables even and odd. Then, there is a nested for loop to check if each integer is a palindrome and update the parity (1 for even, 2 for odd) and the list of such integers and their parities. Finally, the given example and test cases are handled to input an integer n and print the result.