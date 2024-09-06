
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    # Initialize histogram variable
    histogram = {}

    # Initialize letter 'a'
    a_count = 0

    # Initialize letter 'b'
    b_count = 0

    # Initialize letter 'c'
    c_count = 0

    # Initialize letter 'd'
    d_count = 0
    
    # Initialize letter 'e'
    e_count = 0

    # Initialize letter 'f'
    f_count = 0

    # Initialize letter 'g'
    g_count = 0

    # Initialize letter 'h'
    h_count = 0

    # Initialize letter 'i'
    i_count = 0

    # Initialize letter 'j'
    j_count = 0

    # Initialize letter 'k'
    k_count = 0

    # Initialize letter 'l'
    l_count = 0

    # Initialize letter 'm'
    m_count = 0

    # Initialize letter 'n'
    n_count = 0

    # Initialize letter 'o'
    o_count = 0

    # Initialize letter 'p'
    p_count = 0

    # Initialize letter 'q'
    q_count = 0

    # Initialize letter 'r'
    r_count = 0

    # Initialize letter 's'
    s_count = 0

    # Initialize letter 't'
    t_count = 0

    # Initialize letter 'u'
    u_count = 0

    # Initialize letter 'v'
    v_count = 0

    # Initialize letter 'w'
    w_count = 0

    # Initialize letter 'x'
    x_count = 0

    # Initialize letter 'y'
    y_count = 0

    # Initialize letter 'z'
    z_count = 0

    for letter in test:

        # Increment 'a' count
        if letter == 'a':
            a_count += 1

        # Increment 'b' count
        if letter == 'b':
            b_count += 1

        # Increment 'c' count
        if letter == 'c':
            c_count += 1

        