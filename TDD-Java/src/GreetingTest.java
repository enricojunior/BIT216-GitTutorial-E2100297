public class GreetingTest {
    private Greeting greeting;

    @Test
    public void getMessage_whenInitializedWithGreeting_returnsGreeting() {
        greeting = new Greeting("Hello world!");
        assertThat(greeting.getMessage(), is("Hello world!"));
    }
}
