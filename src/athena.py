from athena_mcp.server import create_server as create_base_server
from instructions import register_instructions

def create_extended_server():
    """Create server with additional instructions."""
    mcp = create_base_server()

    register_instructions(mcp)

    return mcp

def main():
    """Main entry point for extended server."""
    print("🚀 Starting Extended AWS Athena MCP Server...")
    mcp = create_extended_server()
    print("📖 Added custom instruction resources:")
    print("   • athena://usage-guide")
    print("   • athena://examples")
    print("   • athena://troubleshooting")
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()