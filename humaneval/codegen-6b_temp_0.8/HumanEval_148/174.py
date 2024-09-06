
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
    earth = False
    if planet1 in ('Mercury', 'Earth', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'):
        earth = planet1
        if planet2 in ('Mercury', 'Earth', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'):
            if earth == planet1: return tuple()
    if planet1 == 'Mercury': planet1 = 'Earth'
    if planet2 == 'Mercury': planet2 = 'Earth'
    earth_orbit = set(['Earth', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'])
    sol = set()
    orb_1 = set()
    orb_2 = set()
    for i in earth_orbit:
        if i not in orb_1:
            orb_1 = orb_1.union(set(orbit(i, earth)))
        else:
            orb_2 = orb_2.union(set(orbit(i, earth)))
    sol = orb_2.intersection(orb_1)
    sol = set(sol)
    sol = sol.union(set(orbit(planet1, earth)))
    sol = sol.union(set(orbit(planet2, earth)))
    sol = tuple(sorted(sol))
    if sol == tuple():
        sol = tuple()
    return sol

