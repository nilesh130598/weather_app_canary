FROM nginx:alpine

# Remove default nginx config
RUN rm -rf /usr/share/nginx/html/*

# Copy your frontend files
COPY . /usr/share/nginx/html

# Copy your ssl certificates.
# COPY ssl/ /etc/nginx/ssl/
        
# Copy custom nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
# EXPOSE 443

CMD [ "nginx", "-g", "daemon off;" ]
