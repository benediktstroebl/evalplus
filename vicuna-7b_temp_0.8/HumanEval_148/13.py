
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
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 == "Mercury" and planet2 == "Jupiter":
        return planets[1:8]
    elif planet1 == "Jupiter" and planet2 == "Mercury":
        return planets[6:]
    elif planet1 == "Earth" and planet2 == "Venus":
        return planets[3:7]
    elif planet1 == "Venus" and planet2 == "Earth":
        return planets[1:4]
    elif planet1 == "Mars" and planet2 == "Jupiter":
        return planets[2:7]
    elif planet1 == "Saturn" and planet2 == "Uranus":
        return planets[4:8]
    elif planet1 == "Uranus" and planet2 == "Neptune":
        return planets[2:5]
    elif planet1 == "Neptune" and planet2 == "Pluto":
        return planets[1:3]
    else:
        return ()

planet1 = input("Enter the name of the first planet: ")
planet2 = input("Enter the name of the second planet: ")
result = bf(planet1, planet2)
print(result)
