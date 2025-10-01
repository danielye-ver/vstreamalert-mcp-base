def register_instructions(mcp):
    """Add instruction resources to existing server."""

    @mcp.resource("athena://usage-guide")
    def usage_guide() -> str:
        return """
# Athena MCP Usage Guide

## MANDATORY WORKFLOW - Follow These Steps:

### 1. Schema Discovery (ALWAYS START HERE)
- Run `list_tables("database_name")` to see available tables
- Run `describe_table("database", "table")` to understand columns

### 2. Query Execution  
- Start with `SELECT * FROM table LIMIT 10` for exploration
- Use reasonable `max_rows` limits (default 1000)
- Add WHERE clauses to filter data early

### 3. Handle Long-Running Queries
- If `run_query` returns query_execution_id (timeout):
1. Use `get_status(query_id)` to monitor progress
2. When status = "SUCCEEDED", use `get_result(query_id)`

## Cost Control:
- ALWAYS use LIMIT clauses for exploratory queries
- Monitor bytes_scanned in query results
- Use column selection instead of SELECT *
        """

    @mcp.resource("athena://examples")
    def examples() -> str:
        return """
# Essential Query Patterns

## Start Here - Table Discovery:
```sql
-- See all tables
list_tables("your_database")

-- Understand table structure  
describe_table("your_database", "interesting_table")

Basic Exploration:

-- Quick peek at data
SELECT * FROM table_name LIMIT 10

-- Row count
SELECT COUNT(*) FROM table_name

-- Column profiling
SELECT column_name, COUNT(*), COUNT(DISTINCT column_name)
FROM table_name
GROUP BY column_name

Production Queries:

-- Efficient filtering
SELECT col1, col2 FROM table_name
WHERE date_col >= CURRENT_DATE - INTERVAL '7' DAY
LIMIT 1000

-- Aggregation with limits
SELECT category, COUNT(*), AVG(value)
FROM table_name
WHERE partition_col = '2024-01'
GROUP BY category
ORDER BY COUNT(*) DESC
LIMIT 50
    """