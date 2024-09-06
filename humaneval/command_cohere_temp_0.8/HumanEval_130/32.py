```python
def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [1] + tri(n - 1)
    else:
        return [1] + tri(n - 1) + tri(n - 2) + tri(n + 1)
```
The function `tri()` follows the definition of the Tribonacci sequence mentioned in the problem. It uses a recursive approach to calculate the Tribonacci numbers and returns the list of the first `n + 1` numbers of the Tribonacci sequence based on the provided parameters. 
To handle the base cases, the function checks if `n` is 0, 1, or even, returning an empty list or 1 respectively. If `n` is odd, it computes the Tribonacci numbers for `n-1`, `n-2`, and `n+1` and combines them with the base case of 1 to get the Tribonacci sequence for the odd `n`. It continues to build the sequence based on the definition of the Tribonacci sequence. 

Here is a simple test suite to verify the correctness of the function:
```python
def test_tribonacci():
    assert tri(0) == []
    assert tri(1) == [1]
    assert tri(2) == [1, 2]
    assert tri(3) == [1, 3, 2, 8]
    assert tri(4) == [1, 3, 6, 8]
    assert tri(100) == [1, 3, 6, 8, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364, 2145, 3326, 5777, 9138, 14591, 21978, 34739, 59082, 95179, 148598, 217811, 361539, 613260, 983143, 1646212, 2646643, 4498966, 7391959, 11739927, 18604366, 29889553, 47818776, 75991976, 125998369, 20066413, 32790660, 52189299, 83146577, 137440898, 216011449, 341622776, 55279182, 88317639, 147588545, 217964691, 367329920, 61326212, 98313161, 164598611, 264575912, 451418964, 72718043, 1172988328, 1860269751, 298816063, 478172814, 759918860, 1259965110, 200632477, 327889867, 521849318, 831461621, 137440391, 216011337, 341621001, 55279121, 88317551, 147588587, 217964711, 367329908, 61326203, 98313165, 164598627, 264575907, 451418914, 72718031, 1172988216, 1860269697, 298816057, 478172774, 759918850, 1259965176, 200632473, 327889854, 521849251, 831461568, 137440359, 216011309, 341620989, 55279111, 88317549, 147588591, 217964679, 367329866, 61326195, 98313155, 164598609, 264575917, 451418934, 727