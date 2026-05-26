import requests
import json
from typing import Optional, Dict, Any
from enum import Enum

class JokeCategory(Enum):
    """Available joke categories"""
    GENERAL = "general"
    PROGRAMMING = "programming"
    KNOCK_KNOCK = "knock-knock"

class JokeGenerator:
    """
    A simple joke generator using the JokeAPI (https://jokeapi.dev/)
    Supports multiple joke categories and formats
    """
    
    BASE_URL = "https://v2.jokeapi.dev/joke"
    
    def __init__(self, timeout: int = 5):
        """
        Initialize the JokeGenerator
        
        Args:
            timeout: Request timeout in seconds
        """
        self.timeout = timeout
        self.session = requests.Session()
    
    def get_joke(self, category: str = "Any", safe_mode: bool = True) -> Optional[Dict[str, Any]]:
        """
        Fetch a random joke from the API
        
        Args:
            category: Joke category (Any, General, Programming, Knock-Knock, Dark, Pun, Spooky, Christmas)
            safe_mode: If True, excludes explicit and offensive jokes
        
        Returns:
            Dictionary containing joke data or None if request fails
        """
        try:
            params = {
                "safe-mode": str(safe_mode).lower()
            }
            
            url = f"{self.BASE_URL}/{category}"
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get("error"):
                print(f"API Error: {data.get('message', 'Unknown error')}")
                return None
            
            return data
        
        except requests.exceptions.ConnectionError:
            print("Error: Unable to connect to the joke API. Check your internet connection.")
            return None
        except requests.exceptions.Timeout:
            print(f"Error: Request timed out (timeout: {self.timeout}s)")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error: Request failed - {str(e)}")
            return None
        except json.JSONDecodeError:
            print("Error: Failed to parse API response")
            return None
    
    def format_joke(self, joke_data: Dict[str, Any]) -> str:
        """
        Format joke data into a readable string
        
        Args:
            joke_data: Dictionary containing joke information
        
        Returns:
            Formatted joke string
        """
        if joke_data.get("type") == "single":
            return joke_data.get("joke", "No joke found")
        elif joke_data.get("type") == "twopart":
            setup = joke_data.get("setup", "")
            delivery = joke_data.get("delivery", "")
            return f"{setup}\n{delivery}"
        else:
            return "Unknown joke format"
    
    def display_joke_info(self, joke_data: Dict[str, Any]) -> None:
        """
        Display complete joke information including metadata
        
        Args:
            joke_data: Dictionary containing joke information
        """
        print("\n" + "="*60)
        print(f"Category: {joke_data.get('category', 'Unknown')}")
        print(f"Type: {joke_data.get('type', 'Unknown')}")
        print("-"*60)
        print(f"Joke: {self.format_joke(joke_data)}")
        print(f"Safe: {joke_data.get('safe', 'Unknown')}")
        print("="*60 + "\n")
    
    def get_categories(self) -> Optional[Dict[str, Any]]:
        """
        Fetch available joke categories from the API
        
        Returns:
            Dictionary containing available categories or None if request fails
        """
        try:
            url = f"{self.BASE_URL}/categories"
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching categories: {str(e)}")
            return None
    
    def close(self) -> None:
        """Close the session"""
        self.session.close()


def main():
    """Main function to demonstrate the joke generator"""
    generator = JokeGenerator()
    
    print("\n🎭 Welcome to the Random Joke Generator! 🎭\n")
    
    while True:
        print("Options:")
        print("1. Get a random joke (Any category)")
        print("2. Get a Programming joke")
        print("3. Get a General joke")
        print("4. Get a Knock-Knock joke")
        print("5. Get a Dark joke (not safe)")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            joke = generator.get_joke(category="Any", safe_mode=True)
            if joke:
                generator.display_joke_info(joke)
        
        elif choice == "2":
            joke = generator.get_joke(category="Programming", safe_mode=True)
            if joke:
                generator.display_joke_info(joke)
        
        elif choice == "3":
            joke = generator.get_joke(category="General", safe_mode=True)
            if joke:
                generator.display_joke_info(joke)
        
        elif choice == "4":
            joke = generator.get_joke(category="Knock-Knock", safe_mode=True)
            if joke:
                generator.display_joke_info(joke)
        
        elif choice == "5":
            confirm = input("This category contains dark humor. Continue? (y/n): ").lower()
            if confirm == "y":
                joke = generator.get_joke(category="Dark", safe_mode=False)
                if joke:
                    generator.display_joke_info(joke)
        
        elif choice == "6":
            print("\n👋 Thanks for using the Joke Generator! Goodbye!\n")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")
    
    generator.close()


if __name__ == "__main__":
    main()
