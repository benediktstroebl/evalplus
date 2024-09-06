
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
    if planet1 not in planet_orbital_orbit.keys() or planet2 not in planet_orbital_orbit.keys():
        return tuple()
    planet_list = []
    # print(planet_orbital_orbit)
    for planet in planet_orbital_orbit:
        if planet != planet1 and planet != planet2:
            temp_list = []
            for element in planet_orbital_orbit[planet]:
                if element in planet_orbital_orbit[planet1] or element in planet_orbital_orbit[planet2]:
                    temp_list.append(element)
            planet_list.append((temp_list, planet))
    planet_list = sorted(planet_list, key = lambda x: len(x[0]))
    return tuple([x[1] for x in planet_list])

