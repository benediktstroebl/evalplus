
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

    planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet_orbits = [(4, 2441), (10, 457), (9, 608), (6, 371), (13, 699), (16, 690), (19, 25559), (8, 483)]
    if planet1 not in planet_names or planet2 not in planet_names:
        return ()
    planet1_orbit, planet2_orbit = planet_orbits[planet_names.index(planet1)], planet_orbits[planet_names.index(planet2)]
    return tuple(sorted([planet for planet in planet_names if planet_orbits[planet_names.index(planet)] >= planet1_orbit and planet_orbits[planet_names.index(planet)] <= planet2_orbit], key = lambda x: abs(planet1_orbit - planet_orbits[planet_names.index(x)])))

    
