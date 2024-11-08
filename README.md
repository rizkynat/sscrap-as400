# Description

sscrap-as400 is a tool for screen scraping IBM iSeries.
## Note
Based on the author's experience, moving the cursor in IBM AS400 may not work with the move_to() method. Instead, you can use exec_command(b'Tab') to move the cursor to the next input field. If you need to find the coordinates of a specific text location, run the emulator application and check the bottom right corner, where the row and column coordinates are displayed.
## Installation (x3270 Emulator)

Before getting started, read more about  [x3270](https://x3270.miraheze.org/wiki/Main_Page). Use x3270 if you want to view the screen while running the automation.<br/>
To install x3270, run:

```bash
sudo apt-get install x3270
```
Alternatively, if you want to run the process in the background without a window/frame, install s3270:
```bash
sudo apt-get install s3270
```
This tool uses py3270 to interact with x3270, an IBM 3270 terminal emulator and other IBM iSeries tools:
```bash
pip install py3270
```
## Installation (TN5250 Emulator)
TN5250 is a terminal emulator for accessing AS/400 systems. Unlike x3270, it cannot be used with the x3270 tool. Follow the instructions in this [repository](https://github.com/tn5250/tn5250) to install TN5250.
<br/>For interaction with the terminal program, install expect:
```bash
sudo apt-get install expect
```
## Usage
Run the following command depending on your setup:
```bash
python3 x3270.py or ./tn5250.exp 

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
