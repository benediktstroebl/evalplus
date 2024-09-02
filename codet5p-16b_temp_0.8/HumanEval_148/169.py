
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

    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    elif planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    else:
        planetlist = [planet1, planet2]
        planets = []
        for planet in planetlist:
            orbital_period = [i for i in range(len(planetlist)) if planetlist[i] == planet]
            orbital_period = orbital_period[-1] + 1
            if orbital_period <= 8:
                for i in range(orbital_period):
                    if i == orbital_period - 1:
                        planets.append(planetlist[i])
                    else:
                        planets.append(planetlist[i])
                        planets.append(planetlist[i+1])
        return tuple(planets)

