
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
    def planet_orbits(planet1, planet2):
        result = [planet1]
        planet2_index = 0
        for i in range(len(planets)):
            if planets[i] == planet2:
                planet2_index = i
        for i in range(len(planets)):
            if (i < planet2_index and planets[i]!= planet2) or (i > planet2_index and planets[i]!= planet1):
                result.append(planets[i])
        return tuple(result)

