# main - Dockerfile for generate-settings
FROM node:18-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine AS runtime
WORKDIR /app

COPY --from=builder /app/node_modules ./node_modules
COPY . .

RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

USER nextjs

EXPOSE 3000
ENV PORT 3000
ENV NODE_ENV production

CMD ["node", "index.js"]

# Additional Implementation 1760502291

# Code Update 1760502291-21056

# Additional Implementation 1760502291

# Additional Implementation 1760502291

# Additional Implementation 1760502291

# Code Update 1760502292-3045

# Additional Implementation 1760502292

# Code Update 1760502292-15019

# Additional Implementation 1760502292

# Code Update 1760502292-26386

# Additional Implementation 1760502292

# Additional Implementation 1760502292

# Additional Implementation 1760502292

# Additional Implementation 1760502292

# Additional Implementation 1760502292

# Additional Implementation 1760502292

# Additional Implementation 1760502292

# Code Update 1760502292-9149
