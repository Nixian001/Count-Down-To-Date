# Count Down To a Specific Date

I made this by just using stack overflow but couldn't find anything similar to this so I decided to share anyway.

## How to use:

Requires PyGame to work!

just change the date on line 10 to whatever date you need to count down to. For Example

`end_time = datetime.datetime(2024, 10, 22, 0, 0, 0, 0) # Year, Month, Day, Hour, Minute, Second, Time Zone`

this line above counts down to 2024 October 22nd at midnight in GMT+0 (I think...)

you can also add anything to do after the countdown to happen in the if statement starting on line 36. For example:

`os.startfile(<path to file>)`

this would open a file in its normal application. For example an MP3 file to give a sound

Hope this is useful to anyone else!

- Nixian001 ^^
