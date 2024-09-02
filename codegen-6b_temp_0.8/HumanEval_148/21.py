
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
    if planet1 not in PLANETS or planet2 not in PLANETS:
        return ()
    s = {}

    def f(o_rel, obj_rel, planet_orbit, s):
        if planet_orbit not in s:
            s[planet_orbit] = (obj_rel, )
        else:
            s[planet_orbit] += obj_rel,
        for obj in o_rel:
            if obj != "Sun":
                if obj not in s:
                    s[obj] = (o_rel, )
                else:
                    s[obj] += o_rel

    planets = set(PLANETS)
    planets.remove("Sun")
    planet1_orbit = PLANETS.index(planet1)
    planet2_orbit = PLANETS.index(planet2)
    #planet_orbit_set = set(PLANETS[:planet1_orbit] + PLANETS[planet1_orbit+1:planet2_orbit] + PLANETS[planet2_orbit+1:])
    planet_orbit_set = set(PLANETS[planet1_orbit:planet2_orbit])
    planet_orbit_set.remove("Sun")
    planet_orbit_set = sorted(list(planet_orbit_set))

    for i in range(planet1_orbit):
        f(PLANETS[i], PLANETS[i+1:], PLANETS[i], s)
    for i in range(planet2_orbit, len(PLANETS)):
        f(PLANETS[i], PLANETS[i-1:], PLANETS[i], s)
    #for i in planet_orbit_set:
    #    f(PLANETS[i], PLANETS[i+1:], PLANETS[i], s)
    #    f(PLANETS[i], PLANETS[i-1:], PLANETS[i], s)
    inbetween = []
    for orbit in planet_orbit_set:
        if s.get(orbit) is not None:
            inbetween += s.get(orbit)
    return tuple(sorted(inbetween))

