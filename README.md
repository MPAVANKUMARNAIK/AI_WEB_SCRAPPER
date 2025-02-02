# AI_Web_Scraper

An intelligent web scraping tool that combines Selenium-based web scraping with AI-powered content parsing using Ollama LLM. Built with Streamlit for a user-friendly interface.

## 🌟 Features

- Web scraping using Selenium with BrowserStack integration
- Intelligent content parsing using Ollama LLM
- Clean and intuitive Streamlit interface
- Handles CAPTCHAs and dynamic content loading
- Splits large content into manageable chunks
- Customizable content parsing queries

## 🛠️ Prerequisites

- Python 3.7+
- BrowserStack account (for Selenium automation)
- Ollama installed locally

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-web-scraper.git
cd ai-web-scraper
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables (create a `.env` file):
```env
BROWSERSTACK_USERNAME=your_username
BROWSERSTACK_ACCESS_KEY=your_access_key
```

## 🚀 Usage

1. Start the Streamlit application:
```bash
streamlit run main.py
```

2. Enter a website URL in the input field

3. Click "Scrape Website" to fetch the content

4. Once content is scraped, enter your parsing query to extract specific information

5. Click "Parse Content" to get AI-powered results

## 🏗️ Project Structure

```
ai-web-scraper/
├── main.py           # Streamlit application entry point
├── scrape.py        # Web scraping functionality
├── parse.py         # AI parsing functionality
└── requirements.txt # Project dependencies
```

## 💻 Code Components

### Web Scraping (`scrape.py`)
- Uses Selenium with BrowserStack for reliable web scraping
- Handles dynamic content and CAPTCHAs
- Cleans and processes HTML content

### AI Parsing (`parse.py`)
- Integrates with Ollama LLM for intelligent content parsing
- Processes content in chunks to handle large datasets
- Customizable parsing instructions

### User Interface (`main.py`)
- Built with Streamlit for easy interaction
- Two-step process: scraping and parsing
- Dynamic content display and error handling

## ⚙️ Configuration

The project uses several key configurations:

- **BrowserStack**: Requires username and access key
- **Chrome Options**: Configurable browser settings
- **Content Parsing**: Adjustable chunk sizes and parsing parameters

## 📝 Notes

- Ensure your BrowserStack account has adequate testing minutes
- The scraping speed depends on the website's size and complexity
- Large websites might require longer processing times
- Adjust sleep timers based on website loading patterns

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [BrowserStack](https://www.browserstack.com/) for Selenium automation
- [Ollama](https://ollama.ai/) for the LLM integration

This project is licensed under the [MIT License](LICENSE).
