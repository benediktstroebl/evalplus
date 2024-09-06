def string_xor(a, b):
    return subprocess.check_output(['od', '-A', '2', '-N', '2', '-t', 'u', a + ' ' + b]).decode()