def correct_bracketing(brackets):
    """ checks if string of brackets has all pairs correctly matched. """

   
    print("Function Signature:", brackets)
    return all(b != ')' for b in brackets)