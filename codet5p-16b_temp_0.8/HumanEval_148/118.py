
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

    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 in planets and planet2 in planets:
        mercury = 0
        venus = 0
        earth = 0
        mars = 0
        jupiter = 0
        saturn = 0
        uranus = 0
        neptune = 0
        index1 = planets.index(planet1)
        index2 = planets.index(planet2)
        if index2 > index1:
            for i in range(index1 + 1, index2):
                if planets[i] == "Mercury":
                    mercury += 1
                elif planets[i] == "Venus":
                    venus += 1
                elif planets[i] == "Earth":
                    earth += 1
                elif planets[i] == "Mars":
                    mars += 1
                elif planets[i] == "Jupiter":
                    jupiter += 1
                elif planets[i] == "Saturn":
                    saturn +=
