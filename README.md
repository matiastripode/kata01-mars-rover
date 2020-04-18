# kata01-mars-rover

1. Inspired by Jason Gorman in his TDD videos series [Test-Driven Development (TDD) in Python #4 - Duplication & The Rule of Three](https://www.youtube.com/watch?v=f6KHs4aMPpU&list=PL1tIFPlmF4ykpjOJKVDwYkpBIeXsoak6S&index=4)) I decided to follow along his video and implement my own version of Mars Rover Kata.

2. Implemented Mars Rover Kata using Python and following TDD. Kata requirements can be found here https://kata-log.rocks/mars-rover-kata.  
3. Takeways
3.1 Usage of `@parameterized.expand([])` to parameterized tests. A best practice that can be handy is:
- parameterized should follow `AAA` from left to righ (`Arrange`, `Act`, `Assert`), there could be more than `A`parameter per section. As you can see in the example bellow there are two `Arrange` pre-conditions (`Compass` and `Point`), one Act (`MoveCommand`) and one `Assert` (`Point`)

```python
   @parameterized.expand([
        (Compass.S,  Point(0,0), MoveCommand.FORWARD, Point(0, 1)),
        (Compass.S,  Point(1,1), MoveCommand.BACKWARD, Point(1, 0)),
        (Compass.E,  Point(0,0), MoveCommand.FORWARD, Point(1, 0)),
        (Compass.E,  Point(1,1), MoveCommand.BACKWARD, Point(0, 1)),
    ])
    def test04_move_commands(self, initial_facing, initial_point, move_command, ends_position):
        #Arrange
        mars_rover = MarsRover(initial_point, initial_facing)
        #Act
        mars_rover.move(move_command)
        #Assert
        self.assertTrue(mars_rover.current_position() == ends_position)
```

4. **Music** to help you out staying in the `zone` [x-team radio](https://radio.x-team.com/)


## Authors

* **Matias Tripode** - *Initial work* - [My profile in Linkedin](https://www.linkedin.com/in/matiastripode/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* Jason Gorman for his great content in youtube [Codemanship](https://www.youtube.com/channel/UCH6iK78WQAwlK1g-z_dYxHA)
* Hernan Wilkinson for inspiring me to learn TDD  [10pines](https://university.10pines.com/webinars_and_videos) 
