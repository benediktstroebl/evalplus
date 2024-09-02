
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
    # testing for correct planet names
    planets = ('Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune')
    if planet1 not in planets or planet2 not in planets:
        return tuple()
    
    # creating a dictionary for planets and their orbits, and sorting it by orbit
    planets_orbits = {'Mercury': 0, 'Venus': 1, 'Earth': 2, 'Mars': 3, 
                      'Jupiter': 4, 'Saturn': 5, 'Uranus': 6, 'Neptune': 7}
    planets_orbits = sorted(planets_orbits.items(), key=lambda x: x[1])
    
    # returning planets in tuple with correct orbit
    res = ()
    if planets_orbits[0][1] <= planets_orbits[1][1]:
        res += (planets_orbits[0][0],)
    if planets_orbits[1][1] <= planets_orbits[2][1]:
        res += (planets_orbits[1][0],)
    if planets_orbits[2][1] <= planets_orbits[3][1]:
        res += (planets_orbits[2][0],)
    if planets_orbits[3][1] <= planets_orbits[4][1]:
        res += (planets_orbits[3][0],)
    if planets_orbits[4][1] <= planets_orbits[5][1]:
        res += (planets_orbits[4][0],)
    if planets_orbits[5][1] <= planets_orbits[6][1]:
        res += (planets_orbits[5][0],)
    if planets_orbits[6][1] <= planets_orbits[7][1]:
        res += (planets_orbits[6][0],)
    
    return res
