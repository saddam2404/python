# Start from an Ubuntu image
FROM ubuntu:22.04

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    tesseract-ocr \
    curl \
    gnupg \
    ca-certificates \
    nodejs \
    npm \
    git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install n8n globally
RUN npm install -g n8n

# Create a new user (like n8n does)
RUN useradd -m -s /bin/bash node

# Switch to non-root user
USER node

# Set default working directory
WORKDIR /home/node

# Default command
CMD ["n8n"]
