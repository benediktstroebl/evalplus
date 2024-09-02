
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
    def orb(x):
        if x == 'Mercury':
            return m
        if x == 'Venus':
            return v
        if x == 'Earth':
            return e
        if x == 'Mars':
            return mars
        if x == 'Jupiter':
            return j
        if x == 'Saturn':
            return s
        if x == 'Uranus':
            return u
        if x == 'Neptune':
            return n
    if planet1 in planets and planet2 in planets:
        m, v, e, mars, j, s, u, n = orb('Mercury'), orb('Venus'), orb('Earth'), orb('Mars'), orb('Jupiter'), orb('Saturn'), orb('Uranus'), orb('Neptune')
        planets_between = []
        for i in planets:
            if orb(i) <= orb(planet1) < orb(planet2):
                planets_between.append(i)
        planets_between.sort(key=orb)
        return tuple(planets_between)
    return tuple()
