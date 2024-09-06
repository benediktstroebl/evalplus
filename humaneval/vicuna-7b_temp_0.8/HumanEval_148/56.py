
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

    # The first two planets have the shortest orbit
    short_orbit_planets = ["Mercury", "Venus"]

    # The rest of the planets, including the second two, have the longest orbit
    long_orbit_planets = ["Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    # Find the orbits of the two planets
    planet1_orbit = get_orbit(planet1)
    planet2_orbit = get_orbit(planet2)

    # Find the orbits of all the planets in the short_orbit_planets list
    short_orbit_planets_orbit = get_orbit(planet1)
    short_orbit_planets_orbit.append(planet2_orbit)

    # Find the orbits of all the planets in the long_orbit_planets list
    long_orbit_planets_orbit = get_orbit(planet1)
    long_orbit_planets_orbit.append(planet2_orbit)

    # Find the shortest and longest orbits
    short_orbit = min(short_orbit_planets_orbit, key=lambda x: x[2])
    long_orbit = max(long_orbit_planets_orbit, key=lambda x: x[2])

    # Find all the planets whose orbit is between the two orbits
    planets = []
    for orbit in short_orbit_planets_orbit:
        if orbit[0] <= planet2_orbit[2] <= orbit[1]:
            planets.append(orbit[0])
        if orbit[0] <= short_orbit and short_orbit <= orbit[1]:
            planets.append(orbit[0])

    planets.extend(long_orbit_planets_orbit)
    planets.sort(key=lambda x: x[2])

    return planets
