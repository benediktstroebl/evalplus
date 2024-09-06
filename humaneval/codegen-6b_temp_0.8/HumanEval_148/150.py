
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
    # this program does not work correctly because it doesn't properly
    # check if the input planet nameis valid
    # all_planets = ('Sun', 'Mercury', 'Venus', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    # planet1, planet2 = planet1.title(), planet2.title()
    # if planet1 not in all_planets or planet2 not in all_planets:
    #     return ()
    # orbit_planets = []
    # for planet in all_planets:
    #     if planet != planet1 and planet != planet2:
    #         if bf(planet1, planet) and bf(planet2, planet):
    #             orbit_planets.append(planet)

    # return tuple(orbit_planets)

    if planet1 not in ('Sun', 'Mercury', 'Venus', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'):
        return ()
    elif planet2 not in ('Sun', 'Mercury', 'Venus', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'):
        return ()

    # direct code
    orbit_planets = []
    for planet in ('Sun', 'Mercury', 'Venus', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'):
        if planet == planet1:
            orbital_planets = []
        elif planet == planet2:
            break
        if planet != planet1 and planet != planet2:
            orbital_planets = tuple(sorted(
                set(bf(planet1, planet)) & set(bf(planet2, planet))))
            orbit_planets.append(orbital_planets)

    return tuple(orbit_planets)
