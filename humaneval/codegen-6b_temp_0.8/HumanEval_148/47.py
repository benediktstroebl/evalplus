
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
    if planet1 in planets and planet2 in planets:
        planet1Total = 0
        planet2Total = 0
        for planet in planets:
            if planet == planet1:
                planet1Total += 1
            elif planet == planet2:
                planet2Total += 1
        if planet1Total < planet2Total:
            for planet in planets[::-1]:
                if planets.index(planet)+1 <= planet1Total and planets.index(planet)+1 >= planet2Total:
                    return tuple(planets[planet1Total+1:planets.index(planet)-1])
        else:
            for planet in planets:
                if planets.index(planet)+1 <= planet2Total and planets.index(planet)+1 >= planet1Total:
                    return tuple(planets[planets.index(planet)+1:planets.index(planet)-1])
    else:
        return tuple()

