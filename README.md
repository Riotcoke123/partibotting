<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
        <img src="https://github.com/user-attachments/assets/8aefdbc2-8e48-43e9-a549-6df85a4424ac"    alt="PARTI.COM" width="250" height="250">
    <h1>parti.com anti viewbotting</h1>
    <p>parti.com anti viewbotting is a Python script designed to analyze livestream viewer data from the Parti API. It calculates the number of real viewers and fake (bot) viewers based on two configurable viewer ratios: <strong>8:1</strong> and <strong>12:1</strong>. The script then outputs the calculated data in a JSON format.</p>
    <h2>Features</h2>
    <ul>
        <li>Fetches livestream data from the Parti API.</li>
        <li>Calculates real viewers and fake viewers based on two ratios:
            <ul>
                <li><strong>8 fake viewers = 1 real viewer</strong></li>
                <li><strong>12 fake viewers = 1 real viewer</strong></li>
            </ul>
        </li>
        <li>Saves the results to a JSON file for further analysis.</li>
        <li>Configurable user ID input and output file location.</li>
    </ul>
    <h2>Prerequisites</h2>
    <p>Ensure you have Python 3.x installed and the following libraries:</p>
    <ul>
        <li><code>requests</code> for making HTTP requests to the Parti API.</li>
        <li><code>json</code> for saving the analyzed data in JSON format.</li>
    </ul>
    <p>You can install the required libraries using:</p>
    <pre><code>pip install requests</code></pre>
    <h2>How It Works</h2>
    <p>The script works by fetching livestream data from the Parti API for a specified user ID. It then calculates the real and fake viewers based on the viewer count and applies two different ratios:</p>
    <ul>
        <li><strong>8:1 ratio:</strong> For every 8 fake viewers, 1 is considered a real viewer.</li>
        <li><strong>12:1 ratio:</strong> For every 12 fake viewers, 1 is considered a real viewer.</li>
    </ul>
    <p>The results are saved in a <code>.json</code> file on your desktop or a specified directory.</p>
    <h2>Usage</h2>
    <h3>1. Clone the repository</h3>
    <pre><code>git clone https://github.com/Riotcoke123/partibotting.git
cd partibotting</code></pre>
    <h3>2. Modify the script (Optional)</h3>
    <p>If you need to change the user ID or the output file path, you can do so by modifying the <code>user_id</code> and <code>file_path</code> variables in the script.</p>
    <pre><code># Example of modifying user_id and file path
user_id = 352497  # Replace with the desired user ID
file_path = r"bot.json"  # Replace with the desired output file path</code></pre>
    <h3>3. Run the script</h3>
    <p>After ensuring the required dependencies are installed, you can run the script with the following command:</p>
    <pre><code>python botting_script.py</code></pre>
    <p>This will fetch the livestream data, calculate the real and fake viewers, and save the results to <code>bot.json</code> (or another path you specify).</p>
    <h2>Output Format</h2>
    <p>The output is a JSON file containing the following fields:</p>
    <pre><code>{
    "id": "352497",
    "total_viewer_count": 1000,
    "8:1_ratio": {
        "real_viewer_count": 111,
        "bot_viewer_count": 888
    },
    "12:1_ratio": {
        "real_viewer_count": 76,
        "bot_viewer_count": 924
    }
}</code></pre>
    <ul>
        <li><strong>id</strong>: User ID associated with the livestream.</li>
        <li><strong>total_viewer_count</strong>: Total number of viewers on the livestream.</li>
        <li><strong>8:1_ratio</strong>: Breakdown of real and fake viewers based on the <strong>8:1 ratio</strong>.</li>
        <li><strong>12:1_ratio</strong>: Breakdown of real and fake viewers based on the <strong>12:1 ratio</strong>.</li>
    </ul>
    <h2>License</h2>
    <p>This project is open source and available under the <a href="https://www.gnu.org/licenses/agpl-3.0.html">GNU Affero General Public License v3.0</a>.</p>

</body>
</html>
