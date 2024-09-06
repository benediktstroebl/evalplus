
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
    
    G = 6.67384e-11
    
    def planets(planet):
        m = G * planet.mass * planet.orbit
        r = G * planet.mass / m
        v = math.sqrt(G * planet.orbit / planet.mass)
        return (m, v, r)

    def distance(planet1, planet2):
        return math.sqrt((planets(planet1)[0] - planets(planet2)[0])**2 + 
                         (planets(planet1)[1] - planets(planet2)[1])**2 + 
                         (planets(planet1)[2] - planets(planet2)[2])**2)

    def times_to_sun(planet1, planet2):
        m1, v1, r1 = planets(planet1)
        m2, v2, r2 = planets(planet2)
        vmax = max(v1, v2)
        time = distance(planet1, planet2) / max(v1, v2)
        return (time, m1 * time / r1, m2 * time / r2)

    def find_planets(planet1, planet2):
        if planet1 not in planets:
            return []
        if planet2 not in planets:
            return []
        t1, t2, t3 = times_to_sun(planet1, planet2)
        planets = []
        if t1 < 1 and t2 < 1:
            planets.append(planet1)
        while len(planets) != 8:
            for planet in planets:
                m, v, r = planets(planet)
                if len(planets) == 8:
                    break
                if t3 > 1:
                    t1, t2 = t2, t1
                v = v * t1
                if 1 - t2 * t1/ t3 < 1e-12:
                    break
                planets.append(mass / r * (v - t2 * t1 / t3))
        return sorted(planets)

    return find_planets(planet1, planet2)

import unittest
