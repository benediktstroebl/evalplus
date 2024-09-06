```python
def count_distinct_characters(string: str) -> int:
    """
    Count all distinct characters, ignoring case.
    """
    def get_distinct_char_count(text):
        # split the string into lowercase and non-alphanumeric characters
        lc_chars = [char for char in text if char.isalpha() or bare(char) and char.isalpha() and
        bare(char)
        
        # all distinct characters are the count of characters minus the count of lc_chars
        distinct_chars = sum(text[i:j] for i, j in enumerate(text) if j - i <= 1 and lc_chars[j])
        return distinct_chars
    
    if __name__ == "__main__":
        input = "xyzXYZ jerry cars ancine"
        print(get_distinct_char_count(input))
    ```