# ClipShell

I have no clue why I even made this, it was mainly for fun and one specific use case where I wanted to use the command line in school for fun but the teacher was able to see my screen so now I can use the command line from anything basically.

# Usage

Run it in the background then navigate wherever. Try it in a text editor first.

Write "sh::" followed by the command you want to be executed. Eg: "sh::ps -aux"

Copy it to the clipboard. Now paste and the result should be the output of running that command.

Easy as that.

# AI integration

Added feature where text copied to the clipboard starting with "ai::" will be sent to Google Gemini. Responses will be put into the clipboard, same as shell functionality.

To use this, you will need to rename `.env.example` to `.env` and enter your API key. Follow the [getting started instructions](https://pypi.org/project/google-generativeai/) to obtain an API key.