
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    p = {'Mercury': (57910000, 107.40000), 'Venus': (108200000, 108.60000), 'Earth': (149600000, 149.59850), 'Mars': (227940000, 227.96600), 'Jupiter': (778330000, 714.24000), 'Saturn': (1426720000, 602.98000), 'Uranus': (2870650000, 255.46000), 'Neptune': (4503500000, 247.41000)}
    if planet1 not in p:
        return ()
    if planet2 not in p:
        return ()
    planet1_r = p[planet1][0]
    planet2_r = p[planet2][0]
    result = []
    for planet in p:
        if planet1_r <= p[planet][0] <= planet2_r:
            result.append(planet)
    return tuple(sorted(result))
