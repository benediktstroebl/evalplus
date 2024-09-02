
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
    if planet1 == "Mercury" or planet1 == "Venus" or planet1 == "Earth" or planet1 == "Mars" or planet1 == "Jupiter" or planet1 == "Saturn" or planet1 == "Uranus" or planet1 == "Neptune":
        if planet2 == "Mercury" or planet2 == "Venus" or planet2 == "Earth" or planet2 == "Mars" or planet2 == "Jupiter" or planet2 == "Saturn" or planet2 == "Uranus" or planet2 == "Neptune":
            if planet1 == "Mercury":
                planet1 = 0
            elif planet1 == "Venus":
                planet1 = 1
            elif planet1 == "Earth":
                planet1 = 2
            elif planet1 == "Mars":
                planet1 = 3
            elif planet1 == "Jupiter":
                planet1 = 4
            elif planet1 == "Saturn":
                planet1 = 5
            elif planet1 == "Uranus":
                planet1 = 6
            elif planet1 == "Neptune":
                planet1 = 7
            if planet2 == "Mercury":
                planet2 = 0
            elif planet2 == "Venus":
                planet2 = 1
            elif planet2 == "Earth":
                planet2 = 2
            elif planet2 == "Mars":
                planet2 = 3
            elif planet2 == "Jupiter":
                planet2 = 4
            elif planet2 == "Saturn":
                planet2 = 5
            elif planet2 == "Uranus":
                planet2 = 6
            elif planet2 == "Neptune":
                planet2 = 7
            if planet2 < planet1:
                planet2 += 8
                planet1 += 8
            planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
            return tuple(planets[planet1:planet2])
        else
