
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
    planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 in planet_list and planet2 in planet_list:
        planet1_index = planet_list.index(planet1)
        planet2_index = planet_list.index(planet2)
        planet1_orbit_radius = planet_list[(planet1_index + 1) % (len(planet_list) - 1)]
        planet2_orbit_radius = planet_list[(planet2_index + 1) % (len(planet_list) - 1)]
        common_orbit_radius = planet_list[planet1_index]
        return tuple(sorted(set([planet1, planet2]).intersection(set(planet_list[planet1_index:planet2_index + 1])), key=lambda planet: planet_list.index(planet)))
    else:
        return ()

