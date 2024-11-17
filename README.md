# Hadeeth Sharing Bot

## Overview
Hadeeth Sharing Bot is a Python-based script that automatically fetches random Hadeeth (Prophetic traditions) from the **Sunnah.com API** and posts them to a designated Facebook page. The bot utilizes automation tools to schedule daily posts, allowing effortless sharing of valuable knowledge.

## Features
- **Random Hadeeth Retrieval**: Fetches random Hadeeth in both English and Arabic from Sunnah.com.
- **Facebook Integration**: Automatically posts the Hadeeth to a Facebook page.
- **Daily Automation**: Uses a scheduler to post at a specified time every day.

## Prerequisites
- Python 3.x installed on your system.
- Access to the **Sunnah.com API** with a valid API key.
- A Facebook page with a valid access token and page ID.

## Installation
1. Clone the repository:
    ```bash
    git clone hhttps://github.com/EthicalYuu/hadeeth-sharing-bot.git
    ```

2. Install the required dependencies:
    ```bash
    pip install requests schedule
    ```

3. Replace placeholders in the script:
    - Update the `page_id_1` and `facebook_access_token_1` variables with your Facebook page ID and access token.
    - Replace the `x-api-key` in the headers with your Sunnah.com API key.

## Usage
1. **Schedule Daily Posts**: 
    - Modify the `schedule_posts` function to set the desired time for daily posting in `HH:MM` format (24-hour clock). 
      Example:
      ```python
      schedule_posts('08:00')  # Posts daily at 8:00 AM.
      ```

2. **Run the Script**:
    - Start the bot by running the script:
      ```bash
      python hadeeth_bot.py
      ```

3. **Automation in Action**:
    - The script will fetch a random Hadeeth, clean the text, and post it to your Facebook page at the scheduled time.

## Code Highlights
### Posting to Facebook
The `post_to_page` function sends an HTTP POST request to Facebook's Graph API, posting the content to the specified page.

### Hadeeth Retrieval
The `gen_hadith` function:
- Sends an HTTP GET request to the Sunnah.com API.
- Cleans the retrieved Hadeeth of HTML tags using a regular expression.
- Combines the English and Arabic texts for the post.

### Scheduling
The `schedule_posts` function automates posting by scheduling the `gen_post_to_page` function at a specified time using the `schedule` library.

## Example Post Format
Below is an example of how the Hadeeth will appear on your Facebook page:

> Narrated Abu Huraira: The Prophet (ﷺ) said, "Whoever believes in Allah and the Last Day should not harm his neighbor..."
>  
> "عَنْ أَبِي هُرَيْرَةَ، قَالَ قَالَ النَّبِيُّ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ ‏"‏ مَنْ كَانَ يُؤْمِنُ بِاللَّهِ وَالْيَوْمِ الآخِرِ فَلاَ يُؤْذِي جَارَهُ‏"

## Further Improvements
- **Code Refactoring**: The current code was written when I first started programming, and it can be refactored for better readability, efficiency, and maintainability. This includes restructuring functions, improving variable naming, and following best coding practices.
- **Error Handling**: Add robust error handling for API requests and Facebook posts to manage issues like rate limits or invalid tokens.
- **Customization**: Allow users to customize the post format or include additional metadata (e.g., source reference).
- **Multi-Page Posting**: Expand the bot to handle posting to multiple Facebook pages.
- **Logging**: Implement logging to track posted Hadeeth and any errors that occur.

## Disclaimer
This bot was created for educational and knowledge-sharing purposes. Ensure compliance with **Facebook's API policies** and **Sunnah.com's API terms of use** when using this script.
