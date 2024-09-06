```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    
    def helper(num):
        sequence = []
        while num > 0:
            sequence.append(str(num%10))
            num //= 10
        return ' '.join(sequence)
    
    if __name__ == "__main__":
        n = 5
        print(helper(n))
```