import subprocess

def search_nixpkgs_for_package(query: str) -> str:
    """Search the nixpkgs repository of Nix code for the given package"""

    print("📞 Function called: search_nixpkgs_for_package with query: ", query)
    result = subprocess.run(["nix", "search", "nixpkgs", query], text=True, capture_output=True)
    if result.returncode == 0:
        print("Result: ", result.stdout)
        return result.stdout
    else:
        return f"no results found for query '{query}'"


def web_search(query: str) -> str:
    """Perform a web search with a query"""
    
    print("📞 Function called: web_search with query: ", query)
    try:
        result = subprocess.run(["ddgr", "--json", query], text=True, capture_output=True, timeout=30)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout
        else:
            return f"no search results found for query '{query}'"
    except subprocess.TimeoutExpired:
        return "search timed out"
    except FileNotFoundError:
        return "search tool not found, please install ddgr"


