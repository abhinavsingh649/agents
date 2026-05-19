---
title: career_conversation
app_file: app.py
sdk: gradio
sdk_version: 5.49.1
---

# Career Conversation

## Overview

**Career Conversation** is an AI-powered chatbot that represents you as your professional alter-ego. It's deployed on Hugging Face Spaces and uses OpenAI's GPT-4o-mini model to answer questions about your career, background, skills, and experience as if you were present.

This is a powerful tool for:
- **Career Networking**: Let potential clients, employers, and collaborators chat with your AI assistant
- **Personal Branding**: Extend your professional presence with an intelligent, always-available assistant
- **Lead Generation**: Automatically capture contact information from interested visitors through Pushover notifications

## How It Works

### app.py

The `app.py` file contains the core application logic:

1. **Profile Loading**: Reads your LinkedIn PDF and personal summary from the `me/` directory
2. **Tool Use**: Implements two tools for real-world interaction:
   - **record_user_details**: Captures visitor contact information and sends push notifications
   - **record_unknown_question**: Records questions the AI couldn't answer for future learning
3. **Chat Interface**: Uses Gradio to create an interactive web interface
4. **LLM Integration**: Leverages OpenAI's API with function calling for intelligent tool usage
5. **Notifications**: Sends real-time push notifications via Pushover when visitors interact with your assistant

### Core Features

- **Personalized Responses**: Grounded in your actual LinkedIn profile and career summary
- **Tool-Enabled**: The AI can actively record visitor interactions and unanswered questions
- **Professional Tone**: Maintains a professional demeanor while steering conversations toward meaningful contact
- **Real-Time Notifications**: Get instant alerts on your phone when visitors engage

## Deployment on Hugging Face Spaces

Your app is deployed at: **https://huggingface.co/spaces/abhinavsingh649/career_conversation**

### What This Means

- **Always Online**: Your AI assistant is available 24/7 without needing to run anything locally
- **Zero Maintenance**: Hugging Face handles infrastructure, scaling, and uptime
- **Easy Sharing**: Share a single link with your network; no installation required for visitors
- **Secure Secrets**: Your API keys and tokens are stored securely as Hugging Face secrets

### Accessing Your Space

- Visit the link above to see your live chatbot
- Share the URL in your LinkedIn profile, email signature, portfolio, or business cards
- Monitor interactions through Pushover notifications on your phone

## Customization

To personalize your deployment:

1. **Update Your Profile**: 
   - Replace `me/linkedin.pdf` with your LinkedIn PDF export
   - Update `me/summary.txt` with your professional summary

2. **Change the Name**:
   - Edit the `name = "Abhinav Singh"` line in `app.py` to your name

3. **Modify the System Prompt**:
   - Adjust the system prompt in `app.py` to change tone or add specific instructions

4. **Redeploy**:
   - After making changes, run `uv run gradio deploy` from the 1_foundations folder
   - Answer the interactive prompts to update your Space

## Managing Secrets

Your Hugging Face Space stores three key secrets:

- **OPENAI_API_KEY**: Your OpenAI API key for GPT access
- **PUSHOVER_USER**: Your Pushover user ID
- **PUSHOVER_TOKEN**: Your Pushover application token

To update these after deployment:

1. Visit your Space on Hugging Face
2. Click the ⚙️ Settings icon (top right)
3. Scroll to "Variables and Secrets"
4. Edit or add secrets as needed

## Future Enhancements

Consider these improvements:

- **RAG/Knowledge Base**: Add context from articles, blog posts, or project documentation
- **Database Integration**: Store Q&A pairs and visitor data in a SQL database
- **Additional Tools**: Add integrations like email, calendar, or CRM systems
- **Multi-Agent System**: Combine with evaluator patterns from earlier labs for more sophisticated reasoning
- **Analytics**: Track visitor engagement and popular questions

## Resources

- [Gradio Deployment Guide](https://www.gradio.app/guides/sharing-your-app#hosting-on-hf-spaces)
- [Hugging Face Spaces Documentation](https://huggingface.co/docs/hub/spaces)
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [Pushover Notifications](https://pushover.net/)
