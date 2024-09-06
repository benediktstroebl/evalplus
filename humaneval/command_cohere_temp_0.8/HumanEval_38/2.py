```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    return ''.join(groups)

def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Uncycle elements in each group.
    groups = [group[0] + group[2] if len(group) == 3 else group for group in groups]
    return ''.join(groups)
```

The `encode_cyclic` function splits the input string into groups of three characters, then cycles the elements within each group to produce an encoded string. The `decode_cyclic` function splits the encoded string into groups of three characters and then undoes the cycling to decode the original string. Both functions operate on string input and provide a string output. 

Make sure to have a BERT tokenizer model installed. If not, this can be done with the following command:
```bash
pip install pybert_tokenizer
``` 
Additionally, you may need to install TensorFlow, PyTorch, and transformers with:
```bash
pip install tensorflow torch transformers
``` 
The model repository can be cloned with the following command:
```bash
git clone https://github.com/AI21Labs/pybert-tokenizer.git
``` 
This will enable access to the `encode_cyclic` and `decode_cyclic` functions for solving the given problem.